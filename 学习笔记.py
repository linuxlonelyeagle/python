{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "01caf078",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "78b8df9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "062d8f97",
   "metadata": {},
   "outputs": [],
   "source": [
    "frame = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','c','d'],columns=['Ohio','Texas','California'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ffb2faf4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ohio</th>\n",
       "      <th>Texas</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ohio  Texas  California\n",
       "a     0      1           2\n",
       "c     3      4           5\n",
       "d     6      7           8"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "aa9d950e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ohio</th>\n",
       "      <th>Texas</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ohio  Texas  California\n",
       "a   0.0    1.0         2.0\n",
       "b   NaN    NaN         NaN\n",
       "c   3.0    4.0         5.0\n",
       "d   6.0    7.0         8.0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.reindex(['a','b','c','d'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4100865d",
   "metadata": {},
   "outputs": [],
   "source": [
    "state=['Texas','Utah','California']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2ff09d93",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Texas</th>\n",
       "      <th>Utah</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>7</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Texas  Utah  California\n",
       "a      1   NaN           2\n",
       "c      4   NaN           5\n",
       "d      7   NaN           8"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.reindex(columns=state)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a751bd67",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Texas</th>\n",
       "      <th>Utah</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>520</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>4</td>\n",
       "      <td>520</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>7</td>\n",
       "      <td>520</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Texas  Utah  California\n",
       "a      1   520           2\n",
       "c      4   520           5\n",
       "d      7   520           8"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.reindex(columns=state,fill_value=520)   ##填充nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "aa5e4c73",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Texas</th>\n",
       "      <th>Utah</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>520xiyou</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>4</td>\n",
       "      <td>520xiyou</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>7</td>\n",
       "      <td>520xiyou</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Texas      Utah  California\n",
       "a      1  520xiyou           2\n",
       "c      4  520xiyou           5\n",
       "d      7  520xiyou           8"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.reindex(columns=state,fill_value='520xiyou')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "dec7a314",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ohio</th>\n",
       "      <th>Texas</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ohio  Texas  California\n",
       "a     0      1           2\n",
       "c     3      4           5\n",
       "d     6      7           8"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "dbaff2fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.loc['a','Ohio']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ebbb8221",
   "metadata": {},
   "outputs": [],
   "source": [
    "frame.loc['a','Ohio']=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f9182dfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ohio</th>\n",
       "      <th>Texas</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ohio  Texas  California\n",
       "a     1      1           2\n",
       "c     3      4           5\n",
       "d     6      7           8"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "777575b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "##删除"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4ccfedbf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ohio</th>\n",
       "      <th>Texas</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ohio  Texas  California\n",
       "c     3      4           5\n",
       "d     6      7           8"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame.drop('a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "e9ff7d2c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ohio</th>\n",
       "      <th>Texas</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ohio  Texas  California\n",
       "a     1      1           2\n",
       "c     3      4           5\n",
       "d     6      7           8"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "26111960",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj = pd.Series(np.arange(5),index=['a','b','c','d','e'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "25b07fbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a    0\n",
       "b    1\n",
       "c    2\n",
       "d    3\n",
       "e    4\n",
       "dtype: int64"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "5082fd4b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b    1\n",
       "c    2\n",
       "d    3\n",
       "e    4\n",
       "dtype: int64"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj.drop('a')   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "8c3add8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a    0\n",
       "b    1\n",
       "c    2\n",
       "d    3\n",
       "e    4\n",
       "dtype: int64"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj    ##实际上并没有删除"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f18cb68f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "c    2\n",
       "d    3\n",
       "e    4\n",
       "dtype: int64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj.drop(['a','b'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca42f31a",
   "metadata": {},
   "outputs": [],
   "source": [
    "##不返回，直接操作原对象"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "0be2cad9",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj.drop('a',inplace=True)   ##没友返回，直接删除掉了"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "c807402e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b    1\n",
       "c    2\n",
       "d    3\n",
       "e    4\n",
       "dtype: int64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obj"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f2e475b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e3787a8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43970f72",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86713d7b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0778d41",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "912cf03f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "416f4dd2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54c1210a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "8a54141f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Texas</th>\n",
       "      <th>Utah</th>\n",
       "      <th>California</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>7</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Texas  Utah  California\n",
       "a      1   NaN           2\n",
       "c      4   NaN           5\n",
       "d      7   NaN           8"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c12eae9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-22-2b4fcb3d701d>:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  frame1['Utah']['c']=1\n"
     ]
    }
   ],
   "source": [
    "frame1['Utah']['c']=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a8ac0f2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1c0d32a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0cb63ef",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83503813",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8936d23e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78bfbd25",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c820e354",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
