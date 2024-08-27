import io
from typing import List
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from ..repository import registros as registrosRepository
import pandas as pd

def service_get_registros_join(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    action: str = 'view'
):
    registros = registrosRepository.get_registros_compra_with_joins_as_dataframe(db, skip, limit)
    
    df = pd.read_sql(registros.statement, db.bind)
    df = df.fillna('Null')

    if action == 'view':
        return df.to_dict(orient='records')
    
    elif action == 'download':
        archivo_salida = io.BytesIO()
        with pd.ExcelWriter(archivo_salida, engine="xlsxwriter") as excel_writer:
            nombre_archivo = "Reporte_TGR_DIN.xlsx"
            df.to_excel(
                excel_writer,
                startrow=0,
                merge_cells=False,
                index=False,
                sheet_name="Reporte TGR - DIN",
            )
        archivo_salida.seek(0)
        return StreamingResponse(
            archivo_salida,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={"Content-Disposition": f"attachment; filename={nombre_archivo}"}
        )
    else: 
        return ValueError('Invalid action')