babypandas
==========

Very quick hack, making a pure python implementation of Pandas'
DataFrame/Series (very incomplete and hacky!!)

Note currently doesn't have index support. Just the very, very, very basics.

Hi, I wrote this as I need to rewrite some code to use pure python, instead of
numpy/Pandas for performance reasons. (working with lots of tiny datasets,
not a few medium/big ones). And I really missed the convenience of the 
DataFrame/Series datastructures.

Working with a list of dictionaries just isn't the same.

Found having to call dict constructor in comprehensions to do what I wanted.

e.g.
    
        data = [
            {'a': 1, 'b': 'banana', 'c': 33},
            {'a': 3, 'b': 'cat', 'c': 3},
        ]
        df = DataFrame(data)

        # add a column (scalar)
        data =[dict(row, d=3) for row in data]
        # vs
        df['d'] = 3

        # add a column (list-like)
        vals = [1, 2]
        data = [dict(row, d=v) for row, v in zip(data, vals)]
        # vs
        df['d'] = vals

        # addition of columns
        data = [dict(row, sum=(row['a'] + row['c'])) for row in data]
        # vs
        df['sum'] = df['a'] + df['c']
        
        # map
        data = [dict(row, small=str.lower(row['b])) for row in data]
        # vs
        df['small'] = df['b'].map(str.lower)
        # or
        df['small'] = df['b'].map(lambda x: x.lower())

        # filter
        data = [row for row in data if row['a'] > 1]
        # vs
        df = df[df['a'] > 1]

        # percentage
        tot = sum(row['a'] for row in data)
        data = [dict(row, pct=(100.0 * row[a'] / tot) for row in data]
        # vs
        df['pct'] = 100.0 * df['a'] * df['a'].sum()
