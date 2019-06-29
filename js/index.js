var app = new Vue({
    el: '#form',
    data: {
        ses:"sd"
      
    },
    methods:{
        
        save(event){
            
            var x = new XMLHttpRequest();
            x.open('GET',"data.json");
            x.withCredentials = true;
            var app =this;
            x.onload = function(){
                var data = JSON.parse(x.responseText);
                app.ses = data.name;
        };
        x.send();

        }
    }

   

});