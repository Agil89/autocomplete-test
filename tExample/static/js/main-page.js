document.getElementById('search').addEventListener('input', function () {
    
    var searchInput = document.getElementById('search');
    var inputValue = searchInput.value;
    // console.log(inputValue);
    $.ajax({
        url: 'http://localhost:8000/api/v1.0/objects/',
        method: 'GET',
        data: {
            'inputValue': inputValue,
        },
        success: function (response) {
            console.log(response);
            $('.empty').html('')
            let formDiv = $(`<div class="form-div w-100"><div>`);
            $('.empty').append(formDiv)
            if (inputValue) {
                for (let object of response.data_obj) {
                    $('.form-div').append(`<a class="w-100 mt-1 mb-1" href="#"><span class="ml-3">${object.name}</span></a>`)
                }
            }
        },
        error: function (error_response) {
            console.log(error_response);
        }
    })
});


