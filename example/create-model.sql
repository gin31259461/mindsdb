-- Create ML engine from handler
drop ml_engine sqlpredictor;


create ml_engine sqlpredictor
from
	sqlpredictor;


-- Create model from ML engine
create model mindsdb.test_sqlpredictor
from
	(
		select
			*
		from
			files.iris_train
	) predict Species using engine = 'sqlpredictor';


-- Get model basic detail
select
	*
from
	information_schema.models
where
	name = 'test_sqlpredictor';


-- Get model detail with available tables
describe mindsdb.test_sqlpredictor;


-- Example: get model detail table -> info
describe mindsdb.test_sqlpredictor.info;


-- Other detail table
describe mindsdb.test_sqlpredictor.features;


describe mindsdb.test_sqlpredictor.model;


describe mindsdb.test_sqlpredictor.jsonai;
