from config.app import *
import pandas as pd

# crear un reporte diferente
def GenerateReportVentas(app:App):
    conn=app.bd.getConection()
    query="""
        SELECT 
            p.pais,
            v.product_id,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p
        ON 
            v.postal_code = p.code
        GROUP BY 
            p.pais, v.product_id
        ORDER BY 
            total_vendido DESC;
    """
    df=pd.read_sql_query(query,conn)
    fecha="08-02"
    path=f"/workspaces/workspacepy0125v2/proyecto/files/data-{fecha}.csv"
    df.to_csv(path)
    sendMail(app,path)

def sendMail(app:App,data):
    # cambiar el asunto 
    app.mail.send_email('from@example.com','Reporte','Reporte',data)

# crear un reporte diferente, aquí añado otro        
def GenerateReportDiscount(app: App):
    conn = app.bd.getConection()
    query = """
        SELECT 
            v.product_id,
            AVG(v.discount) AS promedio_descuento
        FROM 
            VENTAS v
        GROUP BY 
            v.product_id
        ORDER BY 
            promedio_descuento DESC;
    """
    df = pd.read_sql_query(query, conn)
    fecha = "08-02"
    path = f"/workspaces/workspacepy0125v2/proyecto/files/discount-{fecha}.csv"
    df.to_csv(path)
    sendMailDiscount(app, path)

    # cambié el asunto 
def sendMailDiscount(app: App, data):
    app.mail.send_email('from@example.com', 'Descuentos', 'Reporte de descuentos', data)