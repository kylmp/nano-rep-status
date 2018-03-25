var data = $('#data').data();

$( document ).ready(function() {
    $.get(data.root+"info", function( data ) {
        updateInfo(data);
    });
    setInterval(function() {
        $.get(data.root+"info", function( data ) {
            updateInfo(data);
        });
    }, 15000);

});

function updateInfo(data) {
	var status = $('#status').html(data.status)
	if (status === "OFFLINE") {
		$('#status').css('color', '#dc3434');
	} else {
		$('#status').css('color', '#4ed259');
		var weight = data.weight/1000000000000000000000000000000;
	    var balance = data.balance/1000000000000000000000000000000;
	    $('#account').html(data.account);
	    $('#representative').html(data.representative);
	    $('#balance').html(balance + " Nano");
	    $('#weight').html(weight + " Nano");
	    $('#peers').html(data.peers);
	    $('#blocks').html(data.blocks);
	    $('#unchecked').html(data.unchecked);
	    $('#version').html(data.version);
	}  
}