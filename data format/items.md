## Item format
For any format docs help, please view [NerdBot Format Types](docs/formats.md)

[Source: Item ID to Name Specifying](data/item_1._source.db)
## All Global Format:
### **Portion #1** *(Item ID to Name Specifing)*:
> Please note that **Item ID** *(len4hex)* is completely diffrent from **Name Specifier** *(b128str)* 

> All spaces in current format case is represented as **"\t"** *(Chr #9)*
```
<(len4hex) ID> <(b128str) NAME>
```
We use a **Item ID** to **Name Specifier** due to nerdbot items' indivudual string name. In this case, it is much easier for nerdbot to identify the **Item ID** *(len4hex)* from the **Name Specifier** *(b128str)* 

### **Portion #2** *(Item Metadata Specifing)*:
> All spaces in current format case is represented as **"\t"** *(Chr #9)*
```
<(len4hex) ID> <(b128str) LANGID_DNAME> <(b128str) LANGID_DESCRIPTION> <(b128int) EMOJIID> [<(len2hex) POCKETID>,<...>,] <(b128int) COST> <(int) RARITY> <(boolean) MULTIUSE>
```
