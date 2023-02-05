from functions import create_connection,execute_select,show_rows

sql_inner_join = """SELECT a.Name, l.Title
                    FROM artists as a
                    INNER JOIN albums as l
                    ON l.ArtistId = a.ArtistId;"""
                    
sql_left_join = """SELECT a.Name, l.Title
                    FROM artists as a
                    LEFT JOIN albums as l ON
                        a.ArtistId = l.ArtistId
                    ORDER BY a.Name;"""

sql_left_join_2 = """SELECT Name, Title
                    FROM artists
                    LEFT JOIN albums ON
                        artists.ArtistId = albums.ArtistId
                    WHERE Title IS NULL  
                    ORDER BY Name;"""
                    
sql_cross_join = """SELECT Name, Title 
                    FROM artists
                    CROSS JOIN albums;"""  
                 
def main():
    titles = ("Name", "Title")
    
    database = "./select_join/chinook.db"

    conn = create_connection(database)
    
    escolha = input("Escolha o exemplo do JOIN (inner,left,left_where,cross): ")
    
    if escolha == "inner":
        sql = sql_inner_join
    elif escolha == "left":
        sql = sql_left_join
    elif escolha == "left_where":
        sql = sql_left_join_2
    elif escolha == "cross":
        sql = sql_cross_join
    
    rows = execute_select(conn,sql)
    
    if "cross" in escolha:
        show_rows(titles,rows,qtd=1000)
    else:
        show_rows(titles,rows)
        
if __name__ == '__main__':
    main()