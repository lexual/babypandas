from babypandas import DataFrame
from babypandas import Series


class TestDF:

    def setup(self):
        self.data = [
            {'a': 1, 'b': 'banana', 'c': 33},
            {'a': 3, 'b': 'cat', 'c': 3},
        ]
        self.df = DataFrame(self.data)

    def test_can_construct(self):
        df = DataFrame()
    
    def test_construct_from_list_of_dicts(self):
        pass

    def test_retrieve_column(self):
        assert self.df['a'] == [1, 3]
        assert self.df['b'] == ['banana', 'cat']

    def test_columns_attribute(self):
        assert set(self.df.columns) == {'a', 'b', 'c'}

    def test_add_column_add(self):
        self.df['d'] = 1
        assert set(self.df.columns) == {'a', 'b', 'c', 'd'}

    def test_set_value_for_existing_column(self):
        self.df['a'] = 1
        assert self.df['a'] == [1, 1]

    def test_set_iterable_for_column(self):
        self.df['a'] = [1, 2]
        assert self.df['a'] == [1, 2]

    def test_remove_column(self):
        del self.df['c']
        assert set(self.df.columns) == {'a', 'b'}

    def test_isin_bool(self):
        assert 'c' in self.df
        assert 'd' not in self.df

    def test_iterate_gives_col_names(self):
        assert set(iter(self.df)) == {'a', 'b', 'c'}

    def test_map_fn(self):
        assert self.df['b'].map(str.upper) == ['BANANA', 'CAT']
        # chain
        assert self.df['b'].map(str.upper).map(str.lower) == ['banana', 'cat']

    def test_addition(self):
        self.df['d'] = self.df['a'] + self.df['c']
        assert self.df['d'] == [34, 6]

    def test_addition_scalar(self):
        self.df['d'] = self.df['a'] + 1
        assert self.df['d'] == [2, 4]

    def test_multiplication(self):
        d = self.df['a'] * self.df['c']
        assert d == [33, 9]

    def test_multiply_scalar(self):
        d = self.df['a'] * 1
        assert self.df['a'] == d
        d = self.df['a'] * 2
        assert d == [2, 6]
        d = 2 * self.df['a']
        assert d == [2, 6]

    def test_bool_comparison_between_series(self):
        result = self.df['a'] == self.df['a']
        assert result == [True, True]

    def test_bool_compare_scalar(self):
        result = self.df['a'] == 1
        assert result == [True, False]
        result = self.df['a'] != 1
        assert result == [False, True]

    def test_bool_gt_etc_compare(self):
        result = self.df['a'] < 2
        assert result == [True, False]
        result = self.df['a'] > 2
        assert result == [False, True]
        result = self.df['a'] < 3
        assert result == [True, False]
        result = self.df['a'] <= 3
        assert result == [True, True]
        #result = self.df['a'] < self.df['c']
        result = self.df['a'] == self.df['a']
        assert result == [True, True]
        result = self.df['a'] < self.df['a']
        assert result == [False, False]

    def test_filter_by_boolean_indexing(self):
        assert len(self.df[True, False]) == 1
        result = self.df[self.df['a'] == 1]
        assert result['a'] == [1]
        assert len(result) == 1

    def test_get_multiple_columns(self):
        subset_df = self.df[['a', 'b']]
        assert set(subset_df.columns) == {'a', 'b'}

    def test_len(self):
        assert len(self.df) == 2
        assert len(DataFrame()) == 0

    def test_divide(self):
        assert Series([2, 4, 6]) / 2 == [1, 2, 3]

    def test_series_sum(self):
        assert self.df['a'].sum() == 4
        #print 1.0 * self.df['a'] / self.df['a'].sum()
