# ConnectionV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**endpoints** | [**list[ConnectionV2Endpoints]**](ConnectionV2Endpoints.md) |  | 
**description** | **str** |  | 
**notifications** | **list[dict(str, object)]** |  | 
**scheduling** | [**ConnectionScheduling**](ConnectionScheduling.md) |  | 
**qos_metrics** | [**dict(str, ConnectionQosMetrics)**](ConnectionQosMetrics.md) |  | 
**paths** | **list[str]** |  | [optional] 
**status** | **str** | Connection Status | [optional] 
**complete** | **bool** |  | [optional] [default to False]
**quantity** | **int** |  | [optional] 
**multi_path** | **bool** |  | [optional] 
**preempt** | **bool** |  | [optional] 
**backup_path_type** | **str** |  | [optional] 
**exclusive_links** | [**list[Link]**](Link.md) |  | [optional] 
**inclusive_links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

