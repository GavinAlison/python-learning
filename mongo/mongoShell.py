'''
filtering, projecting, grouping, sorting, limiting, skipping

'''

db.articles.aggregate({'$project': {'author': 1}},
	{'$group': {'_id': '$author', 'count': {$sum: 1}}},
	{$sort: {count: -1}},
	{$limit: 5}
	)

db.users.aggregate({$project: {userId: $id, _id: 0}})


db.epmloyess.aggregate({
	$project: {
		totalPay: {
			$subtract: [
				{$add: [$salary, $bouns]},
				$401k
			]
		}
	}
})
$add, $subtract, $divide, $mod, $multiply

每个雇员的工作时间
db.employees.aggregate({
	$project: {
		tenure: {
			$subtract: [
				{$year: new Date()},
				{$year: $hireDate}
			]
		}
	}
})


$substr[expr, startOffset, numToReturn]

$concat[expr1, expr2, ..., exprN]

$toLower(expr)

$toUpper(expr)

db.employees.aggregate({
	$project: {
		email: {
			$concat: [
				{$subtract: [$firstname: 0, 1]},
				'.',
				'$lastName',
				'@example.com'
			]
		}
	}
})

logical expression

$cmp: [expr1, expr2]
$strcasecmp: [string1, string2]
$eq/$ne/$gt/$gte/$lt/$lte: [expr1, expr2]
$and: [expr1, expr2, ..., exprN]
$or: [expr1, expr2, ..., exprN]
$not: expr
$ifNull: [expr, replacementExpr]


{$group: {_id: $day}}
{$group: {_id: $grade}}
{$group: {_id: {state: $state, city: $city}}}

db.sales.aggregate({
	$group: {
		_id: $country,
		totalRevence: {$avg: $revence},
		numSales: {$sum: 1}
	}
})


$max/  $min  $last $first
$addToSet
$push

db.log.findOne({
	_id: ObjectId('50eeffc4c82a52712'),
	author: 'k',
	post: 'hello world',
	comments: [
		{
			author: 'mark',
			date: new Date(),
			text: 'Nice post'
		},
		{
			author: 'bill',
			date: new Date(),
			text: 'I agree'
		}
	]
})


$sort
$limit
$skip




# 配置分片
mongo -nodb
cluster  = new ShardingTest({'shards': 3, 'chunksize': 1})
db = (new Mongo('localhost:30999')).getDB('test')
# 启动分片
sh.enableSharding('test')





