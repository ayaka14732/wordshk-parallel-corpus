# Words.hk Cantonese-English Parallel Corpus

## Design

TODO

## Project Structure

```
all (41859) -> minus15 (29487)
            |
            -> plus15 -> train (9372)
                      |
                      -> dev (1500)
                      |
                      -> test (1500)
```

## Build

Download the latest version of words.hk data from the [download page](https://words.hk/faiman/analysis/). Then run:

```sh
gzip -d all-*.csv.gz
python extract.py
python split_train_dev_test.py
python split_15.py
```

## Special Credits

- Hong Kong Cantonese Corpus (HKCanCor)
- [香港大學語言學系](http://www.linguistics.hku.hk/)
- [林璃蝶](https://www.facebook.com/o.indicum)女士
- [Can Cheng](https://twitter.com/cancheng)
- [昭源字體 Chiron Fonts](https://chiron-fonts.github.io/)
- 劉擇明博士
