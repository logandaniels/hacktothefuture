function onUpVote( id ) {
    alert("UPVOTED " + id);
    $.ajax({
        url : "/products/" + productID + "/voteup_proconid=" + id,
        async : true,
        type : "POST"
    });
}

function onLoadSuccess( response ) {
    // Get product details from Target
    var product = response.CatalogEntryView[0];
    
    $("#product-title").text(product.title);
    $("#product-image").attr("src", product.Images[0].PrimaryImage[0].image);
    $("#product-details").append(product.shortDescription);
}

function onLoadError( response ) {
}

function onLoadProsSuccess( response ) {
    $("#pros-table").html("");
    
    if( response == "" ) {
        $("#pros-table").append("<tr><td>This doesn't have any feedback yet.</td></tr>");
    } else {
        response = JSON.parse(response);
        for( var i = 0; i < response.length; i++ ) {
            var item = response[i];
            $("#pros-table").append(
                "<tr><td>" + 
                item.message + 
                "</td><td 'class='col-md-2'><span class='glyphicon glyphicon-arrow-up' id='pro-up" +
                i +
                "'></span> " + 
                item.votes + 
                " <span class='glyphicon glyphicon-arrow-down'></span></td></tr>"
            );
            
            $("#pro-up" + i).click(function() { onUpVote(item.id) });
        }
    }
}

function onLoadProsError( response ) {
}

function onLoadConsSuccess( response ) {
}

function onLoadConsError( response ) {
}

function loadProduct() {
    // Request details from Target
    $.ajax({
        url : "http://api.target.com/v2/products/" +
        productID +
        "?idType=TCIN&key=J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF",
        success : onLoadSuccess,
        error : onLoadError,
        crossDomain : true,
        dataType : "jsonp",
        async : true
    });
    
    // Request list of pros and cons
    $.ajax({
        url : "/products/" + productID + "/gettoppros=3",
        success : onLoadProsSuccess,
        error : onLoadProsError,
        async : true
    });
    $.ajax({
        url : "/products/" + productID + "/gettopcons=3",
        success : onLoadConsSuccess,
        error : onLoadConsError,
        async : true
    });
}