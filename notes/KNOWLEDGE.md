# `const` vs. `let`

In JavaScript, `const` and `let` are two different ways to declare variables, and they have distinct characteristics:

1. `const`:
    - Constant variable declaration.
    - Once assigned, the value cannot be re-assigned or changed.
    - The variable must be assigned a value at the time of declaration; it cannot remain uninitialized.
    - It creates a block-scoped variable.
    - You can still modify the properties of an object or array declared with `const`, but you cannot reassign the variable to another value.

Example:

```javascript
const pi = 3.14;
// pi = 3.1415;  // This will throw an error since reassignment is not allowed.

const person = { name: "John" };
person.age = 30; // Valid, as we are modifying a property of the object.
// person = { name: 'Alice' };  // This will throw an error since reassignment is not allowed.
```

2. `let`:
    - Mutable variable declaration.
    - Allows re-assigning a value to the variable.
    - The variable can be declared without an initial value and assigned later.
    - It also creates a block-scoped variable.

Example:

```javascript
let count = 0;
count = 10; // Valid, since 'let' allows re-assignment.

let x; // Declaration without an initial value
x = 42; // Assigning a value later
```

The choice between `const` and `let` depends on the use case and the intended behavior of the variable. Generally, it is recommended to use `const` whenever possible, as it promotes immutability and makes the code more predictable and easier to reason about. If you know the variable's value should never change, use `const`. Use `let` when you need to reassign the variable's value during runtime or if the value will change over time.

# Are there non-block-variables in javascript?

In JavaScript, all variables declared using `var`, `let`, and `const` are block-scoped. Block scope means that the variable is only accessible within the block in which it is declared. A block in JavaScript is defined by a set of curly braces `{}` that encompass statements.

Prior to the introduction of `let` and `const` in ECMAScript 6 (ES6), the only way to declare variables was using `var`. Variables declared with `var` are also function-scoped, which means they are accessible within the entire function in which they are declared, regardless of block boundaries.

However, `let` and `const` were introduced in ES6 to provide block-scoped variables, improving the predictability and maintainability of JavaScript code. Now, it is recommended to use `let` and `const` instead of `var` for variable declarations to take advantage of block scoping and avoid potential issues related to function-scoped variables.

Here's an example of block-scoped variables using `let` and `const`:

```javascript
// Block-scoped variable using 'let'
if (true) {
    let x = 10; // 'x' is accessible only within this block
    console.log(x); // Output: 10
}
// console.log(x); // This will throw an error because 'x' is not accessible outside the block

// Block-scoped variable using 'const'
if (true) {
    const y = 20; // 'y' is accessible only within this block
    console.log(y); // Output: 20
}
// console.log(y); // This will throw an error because 'y' is not accessible outside the block
```

In summary, all variables in modern JavaScript, including `let` and `const`, are block-scoped, ensuring that they are confined to the specific block in which they are declared, promoting better code organization and reducing the risk of unintended side effects.
