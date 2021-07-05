from prettytable import PrettyTable

def create_table(fields: list, data:list):
    tbl = PrettyTable()
    tbl.field_names = fields
    tbl.add_rows(
        [
            ["ASDF", "ASDF"],
            ["LKJH", "LKJH"]
        ]
    )
    str(tbl)
    
    print(tbl)

create_table()