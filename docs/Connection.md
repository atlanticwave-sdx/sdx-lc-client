# Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**ingress_port** | [**Port**](Port.md) |  | 
**egress_port** | [**Port**](Port.md) |  | 
**quantity** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**multi_path** | **bool** |  | [optional] 
**preempt** | **bool** |  | [optional] 
**backup_path_type** | **str** |  | [optional] 
**exclusive_links** | [**list[Link]**](Link.md) |  | [optional] 
**inclusive_links** | [**list[Link]**](Link.md) |  | [optional] 
**bandwidth_required** | **float** |  | [optional] 
**bandwidth_measured** | **float** |  | [optional] 
**latency_required** | **float** |  | [optional] 
**latency_measured** | **float** |  | [optional] 
**packetloss_required** | **float** |  | [optional] 
**packetloss_measured** | **float** |  | [optional] 
**availability_required** | **float** |  | [optional] 
**availability_measured** | **float** |  | [optional] 
**paths** | **list[str]** |  | [optional] 
**status** | **str** | Connection Status | [optional] 
**complete** | **bool** |  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

