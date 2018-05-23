
$(document).ready(function() {
    /* Django jquery code here */
    console.log("ready");
    $('#artist_rec').autocomplete({

        source: function (request, response) {
            var artist_rec = document.getElementById("artist_rec");
            $.ajax({
                url: "http://musicbrainz.org/ws/2/artist",
                type: "GET",
                data: {
                    query: $(artist_rec).val()+"*",
                    limit: "5",
                    fmt: "json"
                },
                success: function(data) {
                 console.log( "success" );
                 var nameArray = [];
                 var i = 0;
                  $.each( data['artists'],function(key,val){
                      nameArray.push({value: val.name , label: val.name , id: val.id});
                   });
                   response(nameArray);
                },
                error: function(XMLHttpRequest, textStatus, errorThrown){ console.log("ajax fail - " + XMLHttpRequest.responseText)}
            });
        },
        minLength: 3,
        select: function( event, ui ) {
        },


    });

    function update(){
    }

});
