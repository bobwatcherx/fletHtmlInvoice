from flet import *
from processprint import printo

def main(page:Page):

	# CREATE TEXTINPUT
	txt_name = TextField(label="YOu Customer name")
	txt_company = TextField(label="YOu COmpany ")


	# CREATE ITEMS INPUT TEXT LIKE UNIT PRICE NAME
	item_txt = Column([
		TextField(label="name items"),
		TextField(label="total items"),
		TextField(label="price items"),

		])

	allitems = []


	# ADD TO ITEMS
	def addtoitem(e):
		# NOW CREATE DICT FROM YOU INPUT AND SEND DICT TO
		# OTHER FUNCTION FOR PRINT YOU INPUT INVOICE
		allitems.append(
			{
				"nama":txt_name.value,
				"company":txt_company.value,
				"items":[
				{	
					# THIS SCRIPT FOR GET VALUE OF INDEX item-txt
					"name":item_txt.controls[0].value,
					"totalpcs":item_txt.controls[1].value,
					"price":item_txt.controls[2].value,

				}]
			}

			)
		# SHOW SnackBar FOR SUCCESS APPEND
		page.snack_bar = SnackBar(	
			Text("success input data"),
			bgcolor="green"
			)
		page.snack_bar.open = True
		page.update()

		# NOW AFTER SUCECSS APEND AND CLEAR TEXT INPUT AGAIN
		txt_name.value = ""
		txt_company.value = ""
		item_txt.controls[0].value = ""
		item_txt.controls[1].value = ""
		item_txt.controls[2].value = ""
		print(allitems)
		page.update()


	# FOR PRINT INVOICE TO PDF
	def printnow(e):
		page.snack_bar = SnackBar(	
			Text("success input data"),
			bgcolor="green"
			)
		page.snack_bar.open = True
		# CREATE FUNCTION FOR SEND PARAM TO FUNCTION 
		printo(allitems)



		page.update()



	page.add(
	Column([
	Text("Invoice Html print pdf",size=30,weight="bold"),
	txt_name,
	txt_company,
	Divider(),
	Text("insert items ",size=20,weight="bold"),
	item_txt,

	ElevatedButton("add To items",
	bgcolor="blue",color="white",
	on_click=addtoitem
	),
	ElevatedButton("EXPORT PDF INVOICE",
	bgcolor="green",color="white",
	on_click=printnow
	)


		])

	)

flet.app(target=main)
