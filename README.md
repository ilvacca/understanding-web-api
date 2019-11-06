# Understanding WebAPIs architectures with Python, Flask & SQLAlchemy

## Introduction
Any software is nowadays embedded between Web Servers and WebAPIs. Communication between services, applications and (web) apps often takes place using **RESTful HTTP protocols**.

The first Python approaches to this world usually occur with **Flask**. A **micro-framework** that - _fortunately_ - allows us to create web applications potentially **far from the monolithic style**.
In fact, when the application starts to become more robust, it emerges the need to **define** and **design an architecture**.

In this repository a small collection of **best practices** and examples of **architectural patterns** to promote the orderly development of WebAPIs.

## Examples
TODO

### 1. Our first Flask server
This is the easiest example that can be realized in Flask: a website with a single route.

#### 1.1. Routes
| NAME | ROUTE |
|---|---|
| Index | / |

### 2. Multiple routing
In this example we extend the possibilities of our website by integrating a second page (_ex. Blog_).

#### 2.1. Routes
| NAME | ROUTE |
|---|---|
| Index | / |
| Blog | /blog |

### 3a. Multiple routing with HTML
It is possible to integrate HTML code into the responses of our website.

#### 3a.1. Routes
| NAME | ROUTE |
|---|---|
| Index | / |
| Blog | /blog |

### 3b. Multiple routing with HTML template
When the web page becomes very complex and starts integrating HTML, CSS or JS code, it may be useful to refer to templates.

#### 3b.1. Routes
| NAME | ROUTE |
|---|---|
| Index | / |
| Blog | /blog |

### 4. Passing arguments
Communication between the users and the website can take place in both directions: inward and outward.
We can pass parameters using a HTTP GET request.

#### 4.1. Routes
| NAME | ROUTE |
|---|---|
| Index | / |
| Blog | /blog |
| Welcome Page | /welcome/<your-name-here> |

### 5. Responding with a JSON (I)
WebApi usually respond through JSON. Let's integrate a small dataset inside the server.

#### 5.1. Routes
| NAME | ROUTE |
|---|---|
| Index | / |
| Welcome Page | /welcome/<your-name-here> |
| Data | /api/data |

**Data access:** variable.

### 6. Passing arguments in a compact way
The number of parameters that are passed to a WebAPI, using the methodology proposed in the example (4), can become many and difficult to interpret. 
The approach shown in this example allows to communicate with a WebAPI in a flexible and easily manageable way.

#### 6. Routes
| NAME | ROUTE | 
|---|---|
| Index | / | 
| Welcome Page Structured | /welcome/<your-name-here> |
| Welcome Page Unstructured | /welcome?user=<your-name-here> | 
| Data | /api/data | 

**Data access:** variable.

### 7. Responding with a JSON (II)

#### 7. Routes
| NAME | ROUTE | 
|---|---|
| Index | / | 
| API - Get all data | /api |
| API - Query user by ID | /api/user?id=<id-here> |

**Data access:** variable.

### 8. Read data from files

#### 8. Routes
| NAME | ROUTE | 
|---|---|
| Index | / | 
| API - Get all data | /api |
| API - Query user by ID | /api/user?id=<id-here> |

**Data access:** CSV and Pandas.

### 9. Read data from a DB

#### 9. Routes
| NAME | ROUTE | 
|---|---|
| Index | / | 
| API - Get all data | /api |
| API - Query user by ID | /api/user?id=<id-here> |

**Data access:** DB and SQLite.

### 10. An architecture with DAO module (SQLite)

### 11. An architecture with DAO and Models (SQLAlchemy)

## Credits

*These resources were created with* ❤ *by Alessio Vaccaro*.
[Website](https://www.alessiovaccaro.com) | [LinkedIn](https://www.linkedin.com/in/alessio-vaccaro/) 