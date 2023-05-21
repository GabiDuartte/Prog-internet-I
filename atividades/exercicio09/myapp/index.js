let Post = class {
    constructor(id, text, likes){
        this.id = id;
        this.text = text;
        this.likes = likes;
}
}

class Microblog {
    constructor(){
        this.posts = []
}

inserir(id,text,likes){
    this.posts.push(new Post(id,text,likes))
}
retrieve(id){
    let indice = -1
    for(let i=0; i<this.posts.length;i++){
        if(this.posts[i].id == id){
            indice = i
            break;
        }
    }
    return indice;
}

update(id,text,likes){
    let indice = this.retrieve(id,text,likes)
    if(indice != -1){
        this.posts[indice] = id,text,likes
    }
}

delete(id){
    let indice = this.retrieve(id)
    if(indice != -1){
        for(let i=indice; i<this.posts.length;i++){
            this.posts[i] = this.posts[i+1];
        }
        this.posts.pop()
    }
}

retrieveAll(){
    return this.posts
}
}

const express = require('express');
const res = require('express/lib/response');
const app = express()

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const router = express.Router();

const port = 3000
app.listen(port, () => {
    console.log(`Aplicação escutando na porta ${port}`)
})


let blog = new Microblog()

function generateRandomText(length) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let text = '';
  
    for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * characters.length);
      text += characters.charAt(randomIndex);
    }
  
    return text;
  }

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

app.get('/posts',  (req, res) => {
    msg = blog.retrieveAll()
    res.json(msg)
});

app.get('/posts/:id', async (req, res) => {
    id = req.params.id
    msg = await blog.retrieve(id)
    if (msg == -1) { 
        res.status(404).json({error: 'Não encontrado'});
     }
    res.json(msg)
});


app.delete('/posts/:id', async function (req, res) {
    id = req.params.id
    msg = blog.delete(id)
    if (msg != -1) {
            msg = await blog.retrieveAll()
            res.json(msg)
            res.status(204).json({error: 'No content'});
    }
    else if (msg == -1) { 
        res.status(404).json({error: 'Não encontrado'}); 
    }
});

app.post('/posts', (req, res) => {
    let id = Date.now();
    let text = generateRandomText(100);
    let likes = getRandomInt(1, 100);
    blog.inserir(id,text, likes)
    res.json({id, text, likes});
});

app.put('/posts/:id', async (req, res) => {
    let id = req.params.id
    let text = generateRandomText(100);
    let likes = getRandomInt(1, 100);
    let msg = await blog.retrieve(id)

    if (msg == -1) { 
        res.status(404).json({error: 'Não encontrado'}); 
    }

    blog.update(id, text, likes);
    res.status(200).json({alterado: 'Post alterado'});
});

app.patch('/posts/:id', (req, res) => {
    let id = req.params.id
    let{text, likes} = req.body;
    let msg = blog.retrieve(id)

    if (msg == -1) { 
        res.status(404).json({error: 'Não encontrado'}); 
    }

    blog.update(id, text, msg.likes)
    res.status(200).json({teste: 'Patch funcionando'});
});

app.patch('/posts/:id/like', async (req, res) => {
    let id = req.params.id
    let {text, likes} = req.body;
    let msg = await blog.retrieve(id)

    if (msg == -1) { 
        res.status(404).json({error: 'Não encontrado'}); 
    }

    blog.update(id, msg.text, likes)
    res.status(200).json({teste: 'Patch funcionando'});
});
