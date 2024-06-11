function mergesort(arr) {
    if (arr.length === 1) {
        return arr;
    }

    let mid = Math.floor(arr.length / 2);
    let left = mergesort(arr.slice(0, mid));
    let right = mergesort(arr.slice(mid));

    return merge(left, right);
}

function merge(first, second) {
    let mix = [];
    let i = 0, j = 0;

    while (i < first.length && j < second.length) {
        if (first[i] < second[j]) {
            mix.push(first[i++]);
        } else {
            mix.push(second[j++]);
        }
    }
    while (i < first.length) {
        mix.push(first[i++]);
    }
    while (j < second.length) {
        mix.push(second[j++]);
    }
    return mix;
}

function result() {
    let arr = [4 , 8 , 1 ,20 , 9 , 5];
    let sortedArr = mergesort(arr);
    console.log(sortedArr);
}

result();
