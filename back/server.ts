import express from 'express'
import router from './router'
import path from 'path'
import cors from 'cors'
const app = express()

app.use(express.json())

app.use(router)
var corsOptions = {
    origin: 'http://127.0.0.1:5000',
    optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
  }
app.use(cors(corsOptions))

app.use('/script.js',(_req:any,res:any,_next:any)=>{
    let dir = __dirname.split('/')
        let pa = ''
        var i = 0 
        console.log(dir)
        for (let d in dir){
            i++
            
            if(i != dir.length-1){
                pa += '/' + dir[i]
                
            }else{
                break
            }
                
        }
    res.set('Content-Type', 'text/javascript').sendFile(path.join(pa + '/script.js'))

})
app.use('/index.css',(_req:any,res:any,_next:any)=>{
    let dir = __dirname.split('/')
        let pa = ''
        var i = 0 
        console.log(dir)
        for (let d in dir){
            i++
            
            if(i != dir.length-1){
                pa += '/' + dir[i]
                
            }else{
                break
            }
                
        }
    res.set('Content-Type', 'text/css').sendFile(path.join(pa + '/index.css'))

})

app.listen(5000, ()=>{})