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
    $('#account').html(data.account);
    $('#representative').html(data.representative);
    $('#balance').html(data.balance);
    $('#weight').html(data.weight);
    $('#peers').html(data.peers);
    $('#blocks').html(data.blocks);
    $('#unchecked').html(data.unchecked);
    $('#version').html(data.version);
}