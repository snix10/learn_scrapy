import json

# Baca file JSON
with open('quotes.json', 'r') as file:
    data = json.load(file)

# Buat file HTML
with open('quotes.html', 'w') as file:
    file.write('<html><head><title>Quotes</title></head><body>')
    file.write('<h1>Quotes</h1>')
    file.write('<table border="1" style="width:100%; border-collapse:collapse;">')
    file.write('<tr><th>Quote</th><th>Author</th><th>Tags</th></tr>')

    # Tambahkan data ke dalam tabel
    for item in data:
        file.write('<tr>')
        file.write(f'<td>{item["text"]}</td>')
        file.write(f'<td>{item["author"]}</td>')
        file.write(f'<td>{", ".join(item["tags"])}</td>')
        file.write('</tr>')

    file.write('</table></body></html>')

print("HTML file has been created successfully!")
