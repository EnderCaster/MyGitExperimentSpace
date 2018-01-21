# create : create class and session.add
# retrieve/select : session(class).filter(class_name.property==xxx)
# 	means select * from class where property=xxx
#	session(class).get(id)
#	means select * from class where pk=id
#	.all means there is no 'where'
# update : first select then modify finally add(the_obj)
#	there is append function for relation
#	append(relation_class(property=xx))
# delete : .get/filter and .delete
