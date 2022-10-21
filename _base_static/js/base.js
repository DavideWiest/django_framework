
auth_token = "";

async function ApiCall(endpoint, query=null) {
    if (auth_token == null) {
        return {sstatus: "error", error: "no auth_token given"}
    }
    if (query == null) {
        url = base_url + endpoint + "?format=json&auth_token=" + auth_token;
    } else {
        url = base_url + endpoint + "?format=json&auth_token=" + auth_token + "&query=" + query;
    }
    var dataresp = await fetch(url).then(response => 
    response.json().then(data => ({
        data: data,
        status: response.status
    })
    ).then(res => {
        var latest_scraped_data = res.data;
        return latest_scraped_data;
    }));
    return dataresp
}

var debounceFunction = function (func, delay) {
    // Cancels the setTimeout method execution
    clearTimeout(timerId)

    // Executes the func after delay time.
    timerId = setTimeout(func, delay)
}

$('input#sl-search-input').on('input', function(e){
    // var $this = $(this);

    // clearTimeout($this.data('timeout'));
    
    debounceFunction(generateSuggestions, 250)

    // $this.data('timeout', setTimeout(function(){
    // }, 500));
});