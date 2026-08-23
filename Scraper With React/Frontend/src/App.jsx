import { useState } from 'react'
// import './App.css'
import Home from './Home.jsx'
import DB from './db_output.jsx' 

function App() {
  var [page,setPage]=useState(1)

  for(let c=0;c<8;c++){
    
  }

  if(page===1){
    return(
            <>
   < Home /> 
    <div onClick={()=>setPage(2)} style={{color:"white",backgroundColor:"green"} } > Check Your Keywords Collection ➡ </div>
    </>

    )
  }

  if(page===2){
    return(
    <>
    <DB/> 
    <div  style={{color:"white",backgroundColor:"green"}}
    onClick={()=>setPage(1)} > ⬅Go Back </div>
    </>)
  }
  
}

export default App
