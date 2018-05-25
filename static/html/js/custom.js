
$(document).ready(function() {
    /* Django jquery code here */
    var idArtist = "none";

    $('#artist_rec').val("");
    $('#rec_rec').val("");

    /* ARTIST FIELD AJAX */
    $('#artist_rec').autocomplete({

        source: function (request, response) {
            var artist_rec = document.getElementById("artist_rec");
            var val = " ";

            if(artist_rec){
                val = $(artist_rec).val();
            }

            $.ajax({
                url: "http://musicbrainz.org/ws/2/artist",
                type: "GET",
                data: {
                    query: val+"*",
                    fmt: "json"
                },
                success: function(data) {
                 var nameArray = [];
                  $.each( data['artists'],function(key,val){
                      nameArray.push({value: val.name , label: val.name , id: val.id});
                   });

                   response(nameArray);
                },
                error: function(XMLHttpRequest, textStatus, errorThrown){ console.log("ajax fail - " + XMLHttpRequest.responseText)}
            });
        },
        minLength: 0,
        change: function( event, ui ) {
            idArtist = ui.item.id;

               /* RECORD FIELD AJAX */
                $('#rec_rec').autocomplete({

                    source: function (request, response) {
                        $.ajax({
                            url: "http://musicbrainz.org/ws/2/recording",
                            type: "GET",
                            data: {
                                query: "arid:"+idArtist,
                                fmt: "json"
                            },
                            success: function(data) {
                                 var nameArray = [];

                                  $.each( data['recordings'],function(key,val){
                                        var flag = true;

                                        $.each( nameArray,function(key2,val2) {

                                           if(String(val2.value) === String(val.title)) {
                                               console.log("F A L S E");
                                                flag = false;
                                            }
                                        });

                                        if( flag ) {
                                            nameArray.push({value: val.title, label: val.title, id: val.id});
                                        }
                                   });
                                  console.log("");
                                  console.log("");
                                  console.log("-----------------------------------------");
                                  console.log("-----------------------------------------");
                                  console.log("count" + nameArray.length);
                                  nameArray = jQuery.unique(nameArray);
                                  console.log("-----------------------------------------");
                                  console.log(data['recording']);
                                  console.log(nameArray);
                                  console.log("count" + nameArray.length);
                                    $.each( nameArray,function(key,val){
                                          console.log(val.title);
                                   });
                                  console.log("-----------------------------------------");
                                   response(nameArray);
                            },
                        });
                    },
                    minLength: 0,
                    select: function( event, ui ) {
                    },
                });
        },

    });






});
