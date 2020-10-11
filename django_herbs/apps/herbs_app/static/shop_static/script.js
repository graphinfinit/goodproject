/*$ (document).ready(
	function() {
		var form = $ ('#form_product');
		function basketUpdating(product_id, number, name, is_delete){
			// Данные для ajax
					var data = {};
					
					
					var csrf_token = $('#form_product [name ="csrfmiddlewaretoken"]').val();
					data["csrfmiddlewaretoken"] = csrf_token;
					data.product_id = product_id;
					data.number = number;
					data.name = name;

					if (is_delete == "true"){
					    data["is_delete"] = "true";
					    }
					
					var url = form.attr("action");


					//  ajax POST запрос и в случае успеха добавление количества товаров в корзине для данной сессии
					
					$.ajax ({ 
					url : url,
					type: 'POST',
					cach: true,
					data: data,
					success: function (data) {
						if (data.products_total_nmb || data.products_total_nmb == 0){
							$('#basket_total_nmb').text('('+ data.products_total_nmb +')')
							$('#gogo ul' ).html("");
							$.each(data.products, function(k, v){
								
							$('#gogo ul' ).append('<li>'+v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'руб.  ' +
								'<a class="delete_item" href="" data-product_id="'+v.id+'" data-name="'+v.name+'"> x </a>'+'</li>')
								});	
						
					}
					},
		
					error: function (data) {
						console.log("error");
					}
		
					});
		
		}








		
		form.on('submit', function(e) {
			e.preventDefault();
			
			
			var number = $('#number').val();
			var submit_btn = $('#submit_btn');
			var product_id = submit_btn.data("product_id");
			var name = submit_btn.data("name");
			
			
			console.log('Product data hi!');
			basketUpdating(product_id, number, name, is_delete = 'false')
			
			
			//$('.basket_items').append('<div>'+name +'  '+ nmb +'ед.    ' + '<a class= "delete_item">x</a>'+'</div>'
	});
	

	$(document).on('click', '.delete_item', function(e) {
		e.preventDefault();
		product_id = $(this).data("product_id")
		name = $(this).data("name")
		number = 0;

		basketUpdating(product_id, number, name = name, is_delete = "true")



	})





	
	});



// Показываем и убираем краткое содержимое корзины
	
$ (document).ready(
	function() {
	$('.basket_container').on('click', function(e) {
		e.preventDefault();
		$(".basket_items").toggleClass('nonvisibility')
	})

	$('.basket_container').mouseover('click', function(e) {
		e.preventDefault();
		$(".basket_items").toggleClass('nonvisibility')
	})





	})
	
	
	
	
	*/
