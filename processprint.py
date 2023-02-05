import pdfkit
def printo(allitems):
	data = allitems

	data_list = ''
	grand_total = 0

	# EXTRACT ALLitems AND SET TO TABLE
	for item in data:
		data_list +=f'<tr><td>{item["nama"]}</td><td>{item["company"]}</td><td><table>'
		for i in item['items']:
			item_price = int(i['price']) * int(i['totalpcs'])
			grand_total +=item_price
			data_list += f'<tr><td><b>name : </b>{i["name"]}</td><td> &nbsp<b> price : </b> ${i["price"]}</td><td>&nbsp<b>per item : </b> {i["totalpcs"]}</td><td>&nbsp<b>Item Price : </b> ${item_price}</td></tr>'

		data_list +='</table></td></tr>'



	# NOW WRITE THE TABLE TO HTML PAGE AND SAVE THE HTML
	with open("data.html",'w') as f:
		f.write(f'''
			<html>
			<head>
			   <title>Data Example</title>
 			   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
			</head>
			<body>
				<div class="container">
				<h1>data invoice html Flet Corporate</h1>
				<table class="table table-striped">
				<thead>
					<th>Name</th>
					<th>Company</th>
					<th>Items</th>
				</thead>

				<tbody>
				{data_list}

				</tbody>
				<tfoot>
				<tr>
					<td colspan="4" align="right">Grand total </td>
					<td>${grand_total}</td>
				</tr>
				</tfoot>


				</table>
				</div>
			</body>
			</html>

			''')
	# NOW SET YOU PAGE LIKE MARGIN  PAGE SIZE  AND OUTLINE

	options = {
	'page-size':"Letter",
	'margin-top':'0in',
	'margin-left':'0in',
	'margin-bottom':'0in',
	'margin-right':'0in',
	'encoding':'UTF-8',
	'no-outline':None

	}


	# FINALLY RENDER TO PDF
	pdfkit.from_file("data.html",'data.pdf',options=options)

