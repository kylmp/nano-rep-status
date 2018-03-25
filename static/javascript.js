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
    var weight = Math.round(data.weight/1000000000000000000000000000000);
    var balance = Math.round(data.balance/1000000000000000000000000000000);
    $('#account').html(data.account);
    $('#representative').html(data.representative);
    $('#balance').html(balance);
    $('#weight').html(weight);
    $('#peers').html(data.peers);
    $('#blocks').html(data.blocks);
    $('#unchecked').html(data.unchecked);
    $('#version').html(data.version);
}