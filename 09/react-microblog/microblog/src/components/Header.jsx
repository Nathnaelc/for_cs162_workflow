// src/components/Header.js
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";

export default function Header() {
  return (
    <Navbar bg="light" sticky="top" className="border-bottom border-secondary">
      <Container>
        <Navbar.Brand>Microblog</Navbar.Brand>
      </Container>
    </Navbar>
  );
}
