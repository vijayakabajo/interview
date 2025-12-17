import { useState } from 'react'

function App(){

  const [form,setForm] = useState({
    email:'',
    password:''
  })

  const [error,setError] = useState({})
  const [loading , setLoading] = useState(false)

  const handleChange=(e)=>{
    setForm({
      ...form,
      [e.target.name]:e.target.value
    })
  }

  const isValid = ()=>{
    let err = {}

    if(!form.email){
      err.email = 'email is required'
    }
    if(!form.password){
      err.password = 'password is required'
    }
    //will add more validation later

    setError(err)
    return Object.keys(err).length===0
  }

  const handleSubmit = async(e)=>{
    e.preventDefault()

    if(!isValid()) return

    setLoading(true)
    setError({})

    try{
      const res = await fetch('http://127.0.0.1:8000/accounts/login',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(form)
      })

      const data = await res.json()

      if(!res.ok || !data.status){
        setError({api:data.message || 'Login failed'})
      }else{
        console.log('Login success',data)
        alert('Login successful')
      }

    }catch(err){
      setError({api:'Server error'})
    }finally{
      setLoading(false)
    }
  }

  return(
    <>
      <form onSubmit={handleSubmit}>

        <input type="email"
          name="email"
          placeholder="email"
          value={form.email}
          onChange={handleChange}
        />
        {error.email && <p style={{color:'red'}}>{error.email}</p>}

        <br/>

        <input type="password"
          name="password"
          placeholder="password"
          value={form.password}
          onChange={handleChange}
        />
        {error.password && <p style={{color:'red'}}>{error.password}</p>}

        <br/>

        {error.api && <p style={{color:'red'}}>{error.api}</p>}

        <button type="submit" disabled={loading}>
          {loading ? 'Logging in...' : 'Login'}
        </button>

      </form>
    </>
  )
}

export default App
