import React, { Component } from "react";
//import Chessboard from "chessboardjsx";
import MoveValidation from "./integrations/MoveValidation";

class App extends Component {
  render() {
    return (
      <div>
        <div style={boardsContainer}>
          <MoveValidation />
        </div>
      </div>
    );
  }
}

export default App;

const boardsContainer = {
  display: "flex",
  justifyContent: "space-around",
  alignItems: "center",
  flexWrap: "wrap",
  width: "100vw",
  marginTop: 30,
  marginBottom: 50
};
