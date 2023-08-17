var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var componentId = this.dataset.component
        var action = this.dataset.action  
        var member = this.dataset.member 
        console.log('componentId:', componentId, 'action:', action , 'member:', member) 

        updateMemberOrder(componentId, action,member)
     }  )
}

function updateMemberOrder(componentId, action, member) {

    var url = /updateComponent/
    fetch(url, {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
            },
        body: JSON.stringify({ 'componentId':componentId, 'action':action, 'member':member})
    })

    .then((Response) => { 
     return Response.json()
     })

    .then((data) => { 
     console.log('data:',data)
     location.reload()      
     })
}