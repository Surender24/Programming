let input = prompt("Enter a positive Number: ")
let num = parseInt(input)

if (isNaN(num) || num < 0) {
    console.log("Please Enter a valid number ");
}
else {
    let count = 0;
    console.log("Odd numbers upto"+ num +": " )
    for(let i = 0;i<=num;i++){
        if(i%2!=0){
            console.log(i);
            count++;
        }
    }
    console.log("Total number of odd Numbers: "+count);
}