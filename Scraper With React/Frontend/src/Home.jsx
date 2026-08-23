import './Home.css'
import React,{useState} from  'react'

const url = "http://127.0.0.1:8000" 

function Table(props){
var count=-1;
var result=props.result
console.log("From Table: ",result)

return(
    <div className="Table">
<table style="width=50%">
<tr key={++count} >
        { result[0]['column_name'].map((i,index)=> {
            console.log("from tables websites",i);
            <b><th key={index} >{{i}}</th></b>
 } )
        }
</tr>


 {
result[1]['rows'].map( (row_array) =>
 (<tr> { row_array.map((i) => {     console.log(" from table : i = ",i);
                                    console.log("from table", row_array );
                                    <td key={++count}>{i}</td>

                                } )
        } </tr>)
)
}


</table>
    </div>
)
}



function Table2(props){
    var data = props.data;
    var keyword = props.keyword;
    var z=[]
    var count=0;
    //var [output,SetOutput] = useState([])

    async function saveData(){
    var temp;
    temp = await fetch(url+'/scraper/saveToDB',{method:"POST"});
    if(temp.status==201){
        alert("Scraped Data Have Been Saved!")
    }else{
       alert("Last Scraped Data Couldn't Saved!")
    }
    }
        z.push(<p><u>Keyword:</u> {keyword} </p>)
        for(const i in data){
        z.push(<u> <b> <ol key={count++} >{i}</ol> </b> </u>)
           for(const j in data[i]){
            //z.push(<li key={count++} > {data[i][j]} </li>)} }
            if(data[i][j].replace(" ","") != ""){
            z.push(<li key={count++} > {data[i][j]} </li>) } }
        }



    return(
    <>
    { z.map((i) => (i))  }
    <button id="button" onClick={saveData}>SAVE</button>
    </>
    )
}

function Home(){
let range = n => Array.from(Array(n).keys())
var x,n,temp1
var result=[]

const url = "http://localhost:8000"
var [input1,setInput1] = useState("")
var [input2,setInput2] = useState("")
var [input,setInput] = useState(" ")
var [response,setResponse] = useState(" No output: ")
var [responseState,setResponseState] = useState(0)
var [buttonState,setButtonState]=useState(<button id="input2" type="submit"  onClick={submitAction}> Submit </button>)

    function handle_input1(event){
    setInput1(event.target.value)}

    function handle_input2(){
    console.log("handle_input2")}

    function handleInput(event){
    setInput(event.target.value)}

    async function submitAction(){
    var temp;
    temp=input
    temp=temp.replace(" ","")
    temp=temp.trim()
    console.log("Checking the input: ",temp)
    if(temp != ''){
            setButtonState(<b style={{backgroundColor:"white",color:"black"}} >Scraping....</b>)
            console.log("...scraping the data")
            //setInput(input.trim())

            x=await fetch(url + '/scraper?keyword='+ input )
            console.log("x=",x)
            console.log("x.status",x.status)
            setButtonState(<button id="input2" type="submit"  onClick={submitAction}> Submit </button>)
            setInput("")
            //console.log( "x.json()",x.json() )



            if(x.status==200){
                x = await x.json()
                result.push({ 'column_name':[] })

                for(const i in x['websites'] ){
                console.log("i in x.webites",i)
                result[0].column_name.push( x.websites[Number(i)] )}

                result.push({'rows':[]})
                for(const j in range(x.max_row) ){
                //temp1= `row${j}`
                result[1]['rows'].push( [] )
                    for(const k in x.data){
                        //console.log("result in for loop",result)
                        //console.log( "result[1]['rows'][j]  ",result[1]['rows'][j] )
                        result[1]['rows'][j].push( x.data[k][j] )
                    }

                }
            console.log("final result : ",result)
            //setResponse(<Table result={result} />)
            setResponse( < Table2 data = {x.data} keyword= {input} /> )


    }
    }


}


return (
<>
        <div id="box1"></div>
        <div id="box2">

        <h1>
            <label>Enter the keyword</label> <br/>
            <input id="input1" type="text" id="keyword" name="keyword" placeholder= "......."
              value={input}  onChange={handleInput}  />
              <br/> <br/>

            <button id="input2" type="submit"  onClick={submitAction}> Submit </button>


        </h1>


        </div>
        <div style={{backgroundColor:"brown"}}>

            <div id="OutputArea">
                {response}
            </div>

        </div>

</>
)

}

export default Home;
