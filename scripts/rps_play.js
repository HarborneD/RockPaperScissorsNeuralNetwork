$( document ).ready(function() {
    $(".option_container").click( function(){submit_choice(this);});
});

function submit_choice(selection)
{
	var awaiting = $("#awaiting_response").val();
	if($("#awaiting_response").val() === "0")
	{

		$("#awaiting_response").val(1);

		var selection_name = selection.id.replace("_container","");
		$("#"+selection_name+"_image").css("border-color","blue");


		var x_values = $("#current_x").val();

		 $.ajax({
		        url: "https://users.cs.cf.ac.uk/HarborneD/rps/cgi-bin/process_rps.py",
		        type: "POST",
		        dataType: "json",
		        data: { selection: selection_name, x_values: x_values},
		        success: function (data) 
		        {
		          	if(data.correct == "1")
		            {
		            	$("#"+selection_name+"_image").css("border-color","green");
		            	$("#play_message").html("You won!");
		            	$("#player_score").html(parseInt($("#player_score").html())+1);
		            }
		            else
		            {
		            	if(data.correct == "0")
			            {
			            	$("#"+selection_name+"_image").css("border-color","orange");
			            	$("#play_message").html("You Tied!");
			            }
			            else
			            {	
			            	$("#"+selection_name+"_image").css("border-color","red");
			            	$("#play_message").html("You lost!");
			            	$("#opponant_score").html(parseInt($("#opponant_score").html())+1);
			            }
		            }

		            $("#question_mark_image").css("display","none");
		            $("#"+data.choice+"_result_image").css("display","block");

		            $("#current_x").val(data.x_values);

		            setTimeout(function(){ 

		            	$("#question_mark_image").css("display","block");
		            	$("#"+data.choice+"_result_image").css("display","none");

		            	$("#"+selection_name+"_image").css("border-color","white");
		            	$("#play_message").html("");

		            	var round_count = parseInt($("#round_count").html());

		            	var current_data = $("#data").val();
	            		if(current_data.length > 0)
	            		{
	            			current_data += "*"
	            		}
	            		current_data += data.fullset
	            		$("#data").val(current_data);

		            	if( round_count < 20)
		            	{
		            		$("#round_count").html(round_count +1);
		            		
		            	}
		            	else
		            	{
		            		$("#play_options_container").css("display","none");
		            		$("#play_message").html("Game Complete!");
							var result_data = $("#data").val();  	

							 $.ajax({
							        url: "https://users.cs.cf.ac.uk/HarborneD/rps/cgi-bin/store_results.py",
							        type: "POST",
							        dataType: "json",
							        data: { result_data: result_data},
							        success: function (data) 
							        {
							        	if(data.stored = "1")
							        	{
							        		alert("Results Stored");
							        	}
							        		
							        }
							});
		            	}
						$("#awaiting_response").val(0);
		            }, 3000);

		           
		        }
		    });

	
	}
	
}
