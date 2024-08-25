import json

# Baca file JSON
with open('quotes.json', 'r') as file:
    data = json.load(file)

# Buat file HTML
with open('quotes.html', 'w') as file:
    file.write('''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quotes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f4f4f4;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Quotes</h1>
    <table>
        <tr><th>Quote</th><th>Author</th><th>Tags</th></tr>
    ''')

    # Tambahkan data ke dalam tabel
    for item in data:
        file.write('<tr>')
        file.write(f'<td>{item["text"]}</td>')
        file.write(f'<td>{item["author"]}</td>')
        file.write(f'<td>{", ".join(item["tags"])}</td>')
        file.write('</tr>')

    file.write('''</table>
</body>
</html>''')

print("HTML file has been created successfully!")
