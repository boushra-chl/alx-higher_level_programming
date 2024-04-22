#!/usr/bin/node
/*
Script that concatenates 2 first arguments
*/
const argument = process.argv;
const result = argument[2] + ' is ' + argument[3];
console.log(result);
