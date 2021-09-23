#PDF data convertion

job no https://www.upwork.com/jobs/~01ffe68e88c87b00f7

Step1:
    get raw data by copying text data from open pdf file
    Text file name should be text.pdf
Step2:
    Run final_convert.py to arrane the data
    you get a file output1.txt




# For json.
# Nr. Nota: note_number
# Folha: page
# Data pregão: trade_date
# ---------
# Negociação: exchange
# C/V: transaction_type
# Especificação do título: asset_description
# Quantidade: quantity
# Preço / Ajuste: price
# Valor operação / Ajuste: trade_value
# --------
# Valor liquido das operações: trade_value
# Taxa de Liquidação: liquidity_fee
# Taxa de Registro: register_fee
# Taxa de termo/opções: options_fee
# Taxa ANA: ana_fee
# Emolumentos: fees /done
# Taxa Operacional: operational_fee /done
# Total Custos / Despesas: total_costs /done
# Liquido para <dd/MM/yyy>: settlement_date : <dd/MM/yyy> done

"""
Proper JSON Format


Data is in name/value pairs
Data is separated by commas
Objects are encapsulated within the opening and closing curly brackets
An empty object can be represented by {}
Arrays are encapsulated within opening and closing square brackets
An empty array can be represented by []
A member is represented by a key-value pair, contained in double quotes
Each member should have a unique key within an object structure
The value of a member must be contained in double quotes, if it's a string
Boolean values are represented using the true or false literals in lower case
Number values are represented using double-precision floating-point format and shouldn't have leading zeroes
"Offensive" characters in a string need to be escaped using the backslash character \
Null values are represented by the null literal in lower case
Dates, and similar object types, aren't adequately supported and should be converted to strings
Each member of an object or array value must be followed by a comma, except for the last one
The standard extension for the JSON file is '.json'
The mime type for JSON files is 'application/json'
"""
