import { useState } from 'react'

function App() {
  const [form, setForm] = useState({
    email: '',
    password: ''
  })

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    //validation
  }

  const isValid = () => {
    err = {}

    if(!form.email) err.email = 'email is required'
    if(!form.password) err.password = 'password is required'
  }


  return (
    <>
      <input 
        type='email'
        placeholder='email'
      /><br />
      <input 
        type='password'
        placeholder='password'
      /><br />

      <button
        type='submit'
      > Login
      </button>
    </>
  )
}

export default App
