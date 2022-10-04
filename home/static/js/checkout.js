$(document).ready(function()
{
$('.PayWithRazorpay').click(function(e){
    e.preventDefault();
    var first_name= $("[name='first_name']").val();
    var last_name= $("[name='last_name']").val();
    var address= $("[name='address']").val();
    var phone= $("[name='phone']").val();
    var city= $("[name='city']").val();
    var country= $("[name='country']").val();
    var amount= $("[name='amount']").val();
    var ordercode= $("[name='ordercode']").val();
    var token= $("[name='csrfmiddlewaretoken']").val();

    if (first_name==''|| last_name==''|| address==''|| phone==''|| city==''|| country==''){
        
        swal("Alert!", "Fill all the Information in shipping form.", "error");
        return false;
    }
    else{
        console.log(amount)
    var options = {
        "key": "rzp_test_iQIsh0VW0lv0GZ", // Enter the Key ID generated from the Dashboard
        "amount": amount * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
        "currency": "INR",
        "name": "Biorite Healthcare",
        "description": "Product Purchase Transaction",
        "order_id": ordercode, //This is a sample Order ID. Pass the `id` obtained in the response of Step 2
        "handler": function (response){
            alert(response.razorpay_payment_id);
            data  ={
                first_name: first_name,
                last_name: last_name,
                address: address,
                phone: phone,
                city: city,
                country: country,
                csrfmiddlewaretoken: token
            }
            $.ajax({
                method:"POST",
                url:"",
                data:data,
                success:function(response){
                    swal("Congratulations!", "Order has been placed. View My order section for more details.", "success").then((value)=>
                    {
                        window.location.href='/home'
                    });
                }
            })
            
        },
        "prefill": {
            "name":first_name+" "+last_name,
            "email": "@",
            "contact": phone
        },
        "notes": {
            "address": "Biorite Healthcare"
        },
        "theme": {
            "color": "#3399cc"
        }
    };
    var rzp1 = new Razorpay(options);
    rzp1.open();
}
    
});
});