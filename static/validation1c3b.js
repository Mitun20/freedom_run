$(".name-note").one("click", function(){
    alert('The name you enter here will be replicated in the certificate. So enter your name with the correct spelling');
 
});

$(document).ready(function() {
    console.log('Script is running...');
    
    $('.membername').each(function(index) {
        // Construct the new name attribute
        var newName = 'name[' + (index + 1) + ']';         
        $(this).attr('name', newName);
    });
});

// Document is ready
$(document).ready(function () {
 $("#individual-price").html("Rs. 500 /-"); 
    $("#get-mem-count").click(function(){
		
		$(".accordion").each(function(){
			var accid = $(this).attr('id');
			//alert(accid);
			if(accid != 'acc_1') {
				//alert(accid);
				$(this).parent(".clone-container").remove();
			}
		});
		
		$('.usernames').val("");
		
        var totalMembers = $('#total-members').val();
        checkmemcount(totalMembers);
    });
    function checkmemcount(checkmemcount_num){
		var team_name = $('#team-name').val();
        if(checkmemcount_num > 4 && team_name != "" && isNaN(team_name)  && checkmemcount_num < 31){
            addmeminfo(checkmemcount_num);
        } else{
            alert ("Minimum 5 Maximum 30 members are allowed and Team Name is Mandatory/Invalid");
        }
    }
    function addmeminfo(valid_memcount){
           
        var one = valid_memcount*500; //5*400 = 2000//            //5*500 = 2500//
        var two = one*0.15;          //2000*0.1 = 200 //        //2500*0.20 = 500 //
        var three = valid_memcount*500; // 5*500 //
        var f_cost = one-two;        // 1800                     // 2500-500 =  2000//                              

        //$("#get-mem-count").prop("disabled",true);
		//$("#team-name").prop("disabled",true);
		//$("#total-members").prop("disabled",true);
        $('.team-mem-form-container').css("display", "block");
        $("#valid_team_mem").text(valid_memcount);
        $("#team-pay-real-cost").text("Rs."+three+"/-");
        $("#team-pay-cost").text("Rs."+f_cost+"/-");
		$('#total_amount').val(f_cost);
		
		//$('.clone-container').remove();
		
        
            var i = 1;
            while (i < valid_memcount ) {
            var acc_id = $('.accordion').last().attr('id');
            var split_id = acc_id.split('_');
            // New index
            var index = Number(split_id[1]) + 1;
            // Create clone
            var newel = $('.clone-container:last').clone(true);
            // Set id of new element aria-labelledby="heading_1" data-parent="#acc_1">
            $(newel).find('.accordion:nth-child(1)').attr("id","acc_"+index);
            $(newel).find('.card-header:nth-child(1)').attr("id","heading_"+index);
            $(newel).find('.header_btn:nth-child(1)').attr("data-target","#collapse_"+index);
            $(newel).find('.header_btn:nth-child(1)').attr("aria-controls","collapse_"+index);
            $(newel).find("#valid_team_mem_current").text(index); 			
						
			$(newel).find(".t_shirt_size_class").attr("id","t_shirt_size_"+index);			
			$(newel).find(".t_shirt_size_select_class").attr("data_id",index);
			
			$(newel).find(".gender_class").attr("id","gender_"+index);
			$(newel).find(".gender_radio_class").attr("data_id",index); 
			$(newel).find(".gender_radio_class").attr("name","gender_radio"+index); 
            
			$(newel).find('.form_title:nth-child(2)').attr("id","collapse_"+index);
            $(newel).find('.form_title:nth-child(2)').attr("aria-labelledby","heading_"+index);
            $(newel).find('.form_title:nth-child(2)').attr("data-parent","#acc_"+index);
            // Insert element
			
            $(newel).insertAfter(".accordion:last");
            i++;
          }
		 // $('.rad_male').attr('checked', true);
		  /* $(".rad_male").each(function(){
			$(this).attr('checked', true);
		  }); */
    }
// Set the date we're counting down to
var countDownDate = new Date("NOV 15, 2022 12:00:00").getTime();


    // Validate Username
    $("#usercheck").hide();
    let usernameError = true;
    $(".usernames").keyup(function () {
        validateUsername();
    });

    // Validate mail
    $("#emailcheck").hide();
    let emailError = true;
    $("#email").keyup(function () {
        validatemail();
    });
    
    // Validate phone
    $("#phonecheck").hide();
    let phoneError = true;
    $("#phone").keyup(function () {
        validatePhone();
    });
    
    // Validate addresas
    $("#addresscheck").hide();
    let addressError = true;
    $("#address").keyup(function () {
        validateAddress();
    });
    
   // Validate location
   $("#locationcheck").hide();
   let locationError = true;
   $("#location").keyup(function () {
       validateLocation();
   });
   
    // Validate coupon
   $("#couponcheck").hide();
   let couponError = true;
   $("#coupon").keyup(function () {
       validateCoupon();
   });

      // Validate dob
      $("#dobcheck").hide();
      let dobError = true;
      $("#dob").keyup(function () {
          validateDOB();
      });   

    
    function validateUsername() {
        let usernameValue = $(".usernames").val();
		var letters = /^[A-Za-z ]+$/;
        if (usernameValue.length == "") {
			$("#usercheck").show();
			usernameError = false;
        } else if (usernameValue.length < 3 || !usernameValue.match(letters)) {
			$("#usercheck").show();
			$("#usercheck").html("**Enter valid Name");
			usernameError = false;
        } else {
			$("#usercheck").hide();
			usernameError = true;
        }
    }

    function validatemail() {
        let emailValue = $("#email").val();
        if (emailValue.length == "") {
			$("#emailcheck").show();
			emailError = false;        
        } else if (emailValue.length < 3) {
			$("#emailcheck").show();
			$("#emailcheck").html("**Enter valid Email");
			emailError = false;
        return false;
        } else if(IsEmail(emailValue)==false){
            $("#emailcheck").show();
            $("#emailcheck").html("**Enter valid Email");
            emailError = false;
            return false;
        } else {
			$("#emailcheck").hide();
			emailError = true;
        }
    }
    
	function IsEmail(emailValue) {
        var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if(!regex.test(emailValue)) {
          return false;
        }else{
          return true;
        }
      }

    function validatePhone() {
        let phoneValue = $("#phone").val();
        if (phoneValue.length == 10  && !isNaN(phoneValue)) {
			$("#phonecheck").hide();
			phoneError = true;
        } else {
			$("#phonecheck").show();
			$("#phonecheck").html("**Enter valid Phone number");
			phoneError = false;   
        }
    }

    function validateAddress() {
        let addressValue = $("#address").val();
        if (addressValue.length == "") {
            $("#addresscheck").show();
			addressError = false;
        } else if (addressValue.length < 3 || !isNaN(addressValue)) {
			$("#addresscheck").show();
			$("#addresscheck").html("**Enter valid Address");
			addressError = false;
        } else {
			$("#addresscheck").hide();
			addressError = true;
        }
    }

    function validateLocation() {
        
        let locationValue = $("#location").val();
        if (locationValue.length == "") {
            $("#locationcheck").show();
			locationError = false;
        } else if (locationValue.length < 3 || !isNaN(locationValue)) {
			$("#locationcheck").show();
			$("#locationcheck").html("**Enter valid Location");
			locationError = false;
        } else {
			$("#locationcheck").hide();
			locationError = true;
        }
    }
    
        function validateCoupon() {
           
        let couponValue = $("#coupon").val();
		
		if (couponValue.length > 3) {
		$.post("check_coupon.html",{coupon: couponValue},function(data,status){
			//alert("Data: " + data + "\nStatus: " + status);			
			if(data != "") {
				$("#couponcheck").show();
				$("#couponcheck").css({"color": "green"});
				$("#couponcheck").html("**Coupon applied !");
				couponError = false;
				var discount1 = (data / 100) * 500;
				var discount2 = 500 - discount1;
				$("#individual-price").html("Rs. "+discount2+" /-");
				$("#individual_amount").val(discount2);				
			} else {
				$("#couponcheck").show();
				$("#couponcheck").css({"color": "red"});
				$("#couponcheck").html("**Enter a Valid Coupon");
				couponError = false;
				$("#individual-price").html("Rs. 500 /-");
				$("#individual_amount").val(500);
			}			
		});
		} else {
			$("#couponcheck").show();
			$("#couponcheck").css({"color": "red"});
			$("#couponcheck").html("**Enter a Valid Coupon");
			couponError = false;
			$("#individual-price").html("Rs. 500 /-");
			$("#individual_amount").val(500);			
		}
		
		
    }
    
    function validateDOB() {
        let dobValue = $("#dob").val();       
        if (dobValue.length < 3 ) {
            $("#dobcheck").show();
            $("#dobcheck").html("**Enter valid DOB");
            dobError = false;
        }  else {
			$("#dobcheck").hide();
			dobError = true;
        }
    }
   
 
    
    // Submit button
    $("#submitbtn").click(function () {
        validateUsername();
        validatemail();
        validatePhone();
        validateAddress();
        validateLocation();
        validateDOB();
		
		if (usernameError == true && emailError == true && addressError == true && phoneError == true && dobError == true &&        locationError == true) {
        return true;
        } else {
        return false;
        }
    });
	
	$('.gender_radio_class').change(function(){
	  var data_id = $(this).attr('data_id');
	  var valu = $(this).val();
	  $('#gender_'+data_id).val(valu);
    });
	
	$('.t_shirt_size_select_class').change(function(){
	  var data_id = $(this).attr('data_id');
	  var valu = $(this).val();
	  $('#t_shirt_size_'+data_id).val(valu);
    });
	
	
	$('.usernames').keyup(function(){
		var usernameValue = $(this).val();
		var letters = /^[A-Za-z ]+$/;		
		if (usernameValue.length == "") {
        $(this).next("p").show();
		$(this).next("p").text("**Enter valid Name");
		$('#is_valid').val(0);
        } else if (usernameValue.length < 3 || !usernameValue.match(letters)) {
        $(this).next("p").show();
        $(this).next("p").text("**Enter valid Name");
		$('#is_valid').val(0);
        } else {
        $(this).next("p").hide();
		$('#is_valid').val(1);
        }	  
    });
	
	
	$('.phones').keyup(function(){
		var usernameValue = $(this).val();  
		if (usernameValue.length == 10 && !isNaN(usernameValue)) {
        $(this).next("p").hide();		
		$('#is_valid').val(1);
        } else {
        $(this).next("p").show();
		$(this).next("p").text("**Enter valid Phone Number");
		$('#is_valid').val(0);
        }	  
    });
	
	
	$('.emails').keyup(function(){
		var usernameValue = $(this).val();  
		if (usernameValue.length < 3) {
			$(this).next("p").show();
			$(this).next("p").html("**Enter valid Email 3");
			$('#is_valid').val(0);
        } else if(IsEmail(usernameValue)==false){
            $(this).next("p").show();
            $(this).next("p").html("**Enter valid Email");
			$('#is_valid').val(0);
        } else {
			$(this).next("p").hide();
			$('#is_valid').val(1);
        }	  
    });

	
	$('.addresss').keyup(function(){
		var usernameValue = $(this).val();  
		if (usernameValue.length < 3 || !isNaN(usernameValue)) {
        $(this).next("p").show();
		$(this).next("p").text("**Enter valid Address");
		$('#is_valid').val(0);
        } else {
        $(this).next("p").hide();
		$('#is_valid').val(1);
        }	  
    });
	
	
	$('.locations').keyup(function(){
		var usernameValue = $(this).val();  
		if (usernameValue.length < 3 || !isNaN(usernameValue)) {
        $(this).next("p").show();
		$(this).next("p").text("**Enter valid Location");
		$('#is_valid').val(0);
        } else {
        $(this).next("p").hide();
		$('#is_valid').val(1);
        }	  
    });
	
	function validate_form() {
		
		var is_valid = $('#is_valid').val();
		if(is_valid == 1) {
			return true;
		} else {
			alert('Enter valid inputs');
			return false;
		}
		
	}
	
	

});
    