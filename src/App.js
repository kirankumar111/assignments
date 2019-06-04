import React, { Component } from 'react'
import { Route } from 'react-router-dom'
import * as BooksAPI from './booksapi'
import './App.css'

//Components
import SearchPage from './bookshelve/searchpage'
import BookList from './bookshelve/booklist'

export default class BooksApp extends Component {

  state = {
    books: []
  }

  componentDidMount(){
    this.fetchMyBooks()
  }

  fetchMyBooks = () => {
    BooksAPI.getAll().then((books) => this.setState({ books }))
  }

  changeShelf = (id,shelf) => {
    BooksAPI.update({id},shelf).then(()=>{
      this.fetchMyBooks()
    })
  }

  render() {
    return (
      <div className="app">
          <Route
            exact
            path="/search"
            render={({history}) => (
              <SearchPage
                myBooks={this.state.books}
                onShelfChange={(id,shelf)=>{
                  this.changeShelf(id,shelf)
                  history.push('/')
                }}
              />
            )}
          />

          <Route
            exact
            path="/"
            render={()=>(
              <BookList
                books={this.state.books}
                onShelfChange={(id,shelf)=>{
                  this.changeShelf(id,shelf)
                }}
              />
            )}
          />
      </div>
    )
  }
}