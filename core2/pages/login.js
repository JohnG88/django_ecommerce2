import {CssBaseline, FormControlLabel, Typography, Button, TextField, Checkbox, Link, Grid, Container, Avatar} from "@material-ui/core";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined"
import { makeStyles } from "@material-ui/styles";

import React, { useState } from "react";
import Router from "next/router";

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center'
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%',
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2)
  },
}));

export const Login = () => {
  const classes = useStyles();  

  const [csrftoken, setCsrfToken] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  React.useEffect(() => {
    fetch('http://localhost:8000/account/csrf/', {
      // shows cookie in browser
      credentials: "include",
    })
      .then((res) => {
        let csrfToken = res.headers.get('X-CSRFToken');
        setCsrfToken(csrfToken);
      })
      .catch((error) => {
        console.log(error);
      })
  }, [])
  console.log('csrftoken', csrftoken)
  function handleSubmit(e) {
    e.preventDefault()
    fetch('http://localhost:8000/account/login/', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      }, 
      credentials: "include",
      body: JSON.stringify({username: username, password: password}),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Connecting problem')
      }
    })
    .then((data) => {
      console.log(data);
      Router.push('/dashboard')
    })
      .catch((err) => {
      console.log(err);
      setError('Could not connect to server.')
    })
  }

  return (
    <>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <div className={classes.paper}>
          {error}
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign In
          </Typography>
          <form className={classes.form} onSubmit={handleSubmit} noValidate>
            <TextField 
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="usename"
              label="Username"
              name="Username"
              autoComplete="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              autoFocus
            /> 
            <TextField 
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="usename"
              label="Username"
              name="Username"
              autoComplete="current-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <FormControlLabel 
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button 
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="#" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </form>
        </div>
      </Container>
    </>
  )
}

export default Login;
