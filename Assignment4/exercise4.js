const strLen = (text) => {
    if (text.length === 0) {
        return 0;
    }
    return strLen(text.substring(1)) + 1;
}
document.querySelector("#display1").innerHTML += "The length of this string is: " + strLen("The length of this string is");