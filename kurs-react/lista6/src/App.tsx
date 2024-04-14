import Header from "./components/Header";
import Products from "./components/Products";
import AddProduct from "./components/AddProduct";

const App = () => {
  return (
    <>
      <Header />
      <main
        style={{
          paddingTop: "4rem",
          paddingBottom: "3rem",
          height: "100%",
        }}
      >
        <Products />
        <AddProduct />
      </main>
    </>
  );
};

export default App;
