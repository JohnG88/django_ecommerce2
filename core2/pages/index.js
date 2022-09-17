import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  example: {
    color: "green",
  }
}));
export default function Home() {
  const classes = useStyles();
  return (
    <div className={classes.example}>
      Hello
    </div>
 )
}
