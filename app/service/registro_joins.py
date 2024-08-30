import io
import time
from typing import Optional
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from ..repository import registros as registrosRepository, sociedad, tipo_archivo, registro_compra
import pandas as pd

def service_get_registros_join(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    action: str = 'view'
):
    start_time = time.time()
    registros = registrosRepository.get_registros_compra_with_joins_as_dataframe(db, skip, limit)
    
    df = pd.read_sql(registros.statement, db.bind)
    df = df.fillna('Null')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")

    if action == 'view':
        return df.to_dict(orient='records')
    
    elif action == 'download':
        archivo_salida = io.BytesIO()
        with pd.ExcelWriter(archivo_salida, engine="xlsxwriter") as excel_writer:
            nombre_archivo = "ReporteJoin.xlsx"
            df.to_excel(
                excel_writer,
                startrow=0,
                merge_cells=False,
                index=False,
                sheet_name="Reporte Registros",
            )
        archivo_salida.seek(0)
        return StreamingResponse(
            archivo_salida,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={"Content-Disposition": f"attachment; filename={nombre_archivo}"}
        )
    else: 
        return ValueError('Invalid action')

def service_get_registros_join_en_df(
    db: Session, 
    skip: Optional[int] = None, 
    limit: Optional[int] = None,
    action: str = 'view'
):
    start_time = time.time()

    query_registros = registro_compra.get_registros_compra(db, skip, limit)
    df_registros = pd.read_sql(query_registros.statement, db.bind)
    df_registros = df_registros.fillna('Null')

    query_sociedad = sociedad.get_sociedades(db, skip, limit)
    df_sociedad = pd.read_sql(query_sociedad.statement, db.bind)
    df_sociedad = df_sociedad.fillna('Null')

    query_tipo_archivos = tipo_archivo.get_tipo_archivos(db, skip, limit)
    df_tipo_archivos = pd.read_sql(query_tipo_archivos.statement, db.bind)
    df_tipo_archivos = df_tipo_archivos.fillna('Null') 

    # Merge the DataFrames
    df_merged = pd.merge(df_registros, df_sociedad, left_on='id_sociedad', right_on='id')
    df_merged = pd.merge(df_merged, df_tipo_archivos, left_on='id_tipo_archivo', right_on='id')
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")

    if action == 'view':
        return df_merged.to_dict(orient='records')
    
    elif action == 'download':
        archivo_salida = io.BytesIO()
        with pd.ExcelWriter(archivo_salida, engine="xlsxwriter") as excel_writer:
            nombre_archivo = "ReporteJoin.xlsx"
            df_merged.to_excel(
                excel_writer,
                startrow=0,
                merge_cells=False,
                index=False,
                sheet_name="Reporte Registros",
            )
        archivo_salida.seek(0)
        return StreamingResponse(
            archivo_salida,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={"Content-Disposition": f"attachment; filename={nombre_archivo}"}
        ) 
    else: 
        return ValueError('Invalid action')