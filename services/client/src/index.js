import React from "react";
import { createRoot } from "react-dom/client";
import { Component } from "react";
import axios from "axios"; // new
import UsersList from "./components/UsersList";
import AddUser from "./components/AddUser";

class App extends Component {
  // updated
  constructor() {
    super();

    this.state = {
      users: [],
      username: "", // new
      email: "", // new
    };

    this.addUser = this.addUser.bind(this); // new
    this.handleChange = this.handleChange.bind(this);
  }

  // new
  componentDidMount() {
    this.getUsers();
  }

  getUsers() {
    axios
      .get(`${process.env.REACT_APP_API_SERVICE_URL}/users`)
      .then((res) => {
        this.setState({ users: res.data });
      }) // updated
      .catch((err) => {
        console.log(err);
      });
  }

  addUser(event) {
    event.preventDefault();

    const data = {
      username: this.state.username,
      email: this.state.email,
    };

    axios
      .post(`${process.env.REACT_APP_API_SERVICE_URL}/users`, data)
      .then((res) => {
        this.getUsers(); // new
        this.setState({ username: "", email: "" }); // new
      })
      .catch((err) => {
        console.log(err);
      });
  }

  handleChange(event) {
    const obj = {};
    obj[event.target.name] = event.target.value;
    this.setState(obj);
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-half">
              <br />
              <h1 className="title is-1">Users</h1>
              <hr />
              <br />
              <AddUser
                username={this.state.username}
                email={this.state.email}
                addUser={this.addUser}
                // eslint-disable-next-line react/jsx-handler-names
                handleChange={this.handleChange}
              />
              <br />
              <br />
              <UsersList users={this.state.users} />
            </div>
          </div>
        </div>
      </section>
    );
  }
}

const container = document.getElementById("root");
const root = createRoot(container);

root.render(<App />);
