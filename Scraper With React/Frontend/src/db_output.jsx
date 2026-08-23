import React, {useState,useEffect} from 'react'

const url = "http://127.0.0.1:8000"

function DB(){


   var [data,setData] = useState([{
   'No keyword saved!: ':
      {
   'Google':[''],
   'DuckDuckGo': [' '],
   'Bing':[''],
   'YouTube':[''],
   'Ebay': [' ']
      }}] )

   var response

   useEffect(() =>
   {fetch(url+'/db').then( data => data.json() ).then(data => setData(data))}   //.then( x => console.log(".then",x) )  }
  ,[] )

   async function deleteKeyword(x){
   console.log("inside deleteKeyword x= ",x)

   x=x.replace('keyword','.')
   x=x.trim()
   x=x.split(" ")

  if(x[1] != ''){
      var keyword=x[1]
      var dateTime=x[2]}
    else{
    var keyword=x[2]
    var dateTime=x[3]}




   var url1 = url +   `/db/delete/${keyword}/${dateTime}`
   response = await fetch(url1,{method:"DELETE" })
   console.log(response)
   console.log(response.status)

      console.log("inside deleteKeyword x= ",x)
      if( response.ok ){
         {fetch(url+'/db').then( data => data.json() ).then(data => setData(data))}
         alert(`${keyword} deleted!`)
         alert("deleted!")
      }else{
         alert(`Couldn't delete ${x}  due to some ERROR!`)
      }
   }

var result=[]

var count=-1

   data.forEach((i,j)=> {
                for(const i1 in i){
                  result.push( <h6  style={{textAlign:"center",fontSize:"22px"}}  onClick={() => deleteKeyword(i1) } key={++count}     > <hr/> {i1}<br/><br/><br/><br/><br/>  </h6> )

                     for(const i2 in i[i1]){

                        result.push( <i> <h6 key={++count}  style={{textAlign:"left",fontSize:"17px"}} >{i2}...</h6> </i> )
                        for(const i3 in i[i1][i2]){
                           result.push(<h6 key={++count}   style={{textAlign:"left"}} > {i[i1][i2][i3]}  </h6>)
                        }                              }
               }

    } )

return(
   <div style={{backgroundColor:'firebrick',color:'black' }}>
    {result.map((i) => (i))}


   </div>
);
}

export default DB;
